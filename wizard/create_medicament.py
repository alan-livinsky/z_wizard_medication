from trytond.model import ModelView, fields
from trytond.pool import Pool
from trytond.wizard import Button, StateAction, StateView, Wizard


class CreateMedicamentStart(ModelView):
    "Inicio de creación de medicamento"
    __name__ = "gnuhealth.create_medicament.start"
    name = fields.Char('Nombre', required=True, help='Nombre del producto')
    active_component = fields.Char(
        'Componente activo', translate=True,
        help='Componente activo principal')

    category = fields.Many2One(
        'gnuhealth.medicament.category', 'Categoría', select=True)

    therapeutic_action = fields.Char(
        'Acción terapéutica', help='Acción terapéutica')

    composition = fields.Text('Composición', help='Componentes')
    indications = fields.Text('Indicaciones', help='Indicaciones')
    strength = fields.Float(
        'Concentración',
        help='Cantidad de medicamento por dosis, por ejemplo 250 mg')

    unit = fields.Many2One(
        'gnuhealth.dose.unit', 'Unidad de dosis',
        help='Unidad de medida para la dosis indicada')

    route = fields.Many2One(
        'gnuhealth.drug.route', 'Vía de administración',
        help='Vía de administración del medicamento')

    form = fields.Many2One(
        'gnuhealth.drug.form', 'Forma farmacéutica',
        help='Forma farmacéutica, por ejemplo tableta, suspensión o líquido')

    sol_conc = fields.Float(
        'Concentración de solución',
        help='Concentración de la solución')

    sol_conc_unit = fields.Many2One(
        'gnuhealth.dose.unit', 'Unidad de concentración',
        help='Unidad de la concentración del medicamento')

    sol_vol = fields.Float(
        'Volumen',
        help='Volumen de la solución')

    sol_vol_unit = fields.Many2One(
        'gnuhealth.dose.unit', 'Unidad de volumen',
        help='Unidad del volumen de la solución')

    dosage = fields.Text(
        'Instrucciones de dosificación', help='Dosificación e indicaciones')
    overdosage = fields.Text('Sobredosis', help='Información sobre sobredosis')
    pregnancy_warning = fields.Boolean(
        'Advertencia de embarazo',
        help='Indica si existe riesgo durante embarazo o lactancia')

    pregnancy = fields.Text(
        'Embarazo y lactancia', help='Advertencias para embarazo y lactancia')

    pregnancy_category = fields.Selection([
        (None, ''),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('X', 'X'),
        ('N', 'N'),
        ], 'Categoría de embarazo',
        help='Categorías de riesgo en embarazo según la clasificación FDA')

    presentation = fields.Text('Presentación', help='Presentación o envase')
    adverse_reaction = fields.Text('Reacciones adversas')
    storage = fields.Text('Condiciones de almacenamiento')
    is_vaccine = fields.Boolean('Es vacuna')
    notes = fields.Text('Información adicional')

    active = fields.Boolean('Activo', select=True)
    dose_presentation = fields.Function(
        fields.Char("Presentación de dosis"),
        "on_change_with_dose_presentation")
    pharmacovigilance_warning = fields.Boolean(
        'Advertencia de farmacovigilancia')

    @fields.depends('strength', 'unit')
    def on_change_with_dose_presentation(self, name=None):
        if self.strength and self.unit:
            return '%s %s' % (self.strength, self.unit.rec_name)
        if self.strength:
            return str(self.strength)
        return ''

    @staticmethod
    def default_active():
        return True

    @staticmethod
    def default_therapeutic_action():
        return 'acción terapéutica'


class CreateMedicamentWizard(Wizard):
    "Asistente de creación de medicamento"
    __name__ = "gnuhealth.create_medicament.wizard"

    start = StateView('gnuhealth.create_medicament.start',
            'z_wizard_medication.gnuhealth_create_medicament_start_view',[
                          Button('Crear', 'create_', 'tryton-ok', default=True),
                          Button('Cancelar', 'end', 'tryton-cancel')
                          ])
    create_ = StateAction('health.gnuhealth_action_view_medicament')

    def do_create_(self, action):
        pool = Pool()
        Template = pool.get('product.template')
        Product = pool.get('product.product')
        UOM = pool.get('product.uom')
        Medicament = pool.get('gnuhealth.medicament')

        try:
            uom, = UOM.search([('name', '=', 'Unit')])
        except:
            uom, = UOM.search([('name', '=', 'Unidad')])

        template = Template()
        template.name = self.start.name
        template.default_uom = uom.id
        template.list_price = 0
        template.save()

        product = Product()
        product.template = template.id
        product.is_medicament = True
        product.save()

        medicament = Medicament()
        medicament.name = product.id
        medicament.active_component = self.start.active_component
        medicament.category = getattr(self.start.category, 'id', None)
        # El campo original no estaba expuesto en el formulario estándar.
        medicament.composition = self.start.composition
        medicament.indications = self.start.indications
        medicament.strength = self.start.strength
        medicament.unit = getattr(self.start.unit, 'id', None)
        medicament.route = getattr(self.start.route, 'id', None)
        medicament.form = getattr(self.start.form, 'id', None)
        medicament.sol_conc = self.start.sol_conc
        medicament.sol_conc_unit = getattr(self.start.sol_conc_unit,
                                           'id', None)
        medicament.sol_vol = self.start.sol_vol
        medicament.sol_vol_unit = getattr(self.start.sol_vol_unit,
                                          'id', None)
        medicament.dosage = self.start.dosage
        medicament.overdosage = self.start.overdosage
        medicament.pregnancy_warning = self.start.pregnancy_warning
        medicament.pregnancy = self.start.pregnancy
        medicament.pregnancy_category = self.start.pregnancy_category
        medicament.presentation = self.start.presentation
        medicament.adverse_reaction = self.start.adverse_reaction
        medicament.storage = self.start.storage
        medicament.is_vaccine = self.start.is_vaccine
        medicament.notes = self.start.notes
        medicament.active = self.start.active
        if getattr(self.start, 'pharmacovigilance_warning', None):
            medicament.pharmacovigilance_warning = \
                self.start.pharmacovigilance_warning
        medicament.save()

        data = {'res_id': [medicament.id]}
        action['views'].reverse()
        return action, data
