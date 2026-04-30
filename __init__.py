from trytond.pool import Pool

from .wizard import create_medicament


def register():
    Pool.register(
        create_medicament.CreateMedicamentStart,
        module='z_wizard_medication', type_='model')
    Pool.register(
        create_medicament.CreateMedicamentWizard,
        module='z_wizard_medication', type_='wizard')
