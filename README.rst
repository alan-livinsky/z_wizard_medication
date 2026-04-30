z_wizard_medication
===================

Propósito
---------

``z_wizard_medication`` concentra el asistente personalizado para dar de alta
medicamentos en GNU Health a partir de un único formulario.

Funcionalidad incluida
----------------------

* Asistente ``gnuhealth.create_medicament.wizard``.
* Formulario de captura de datos del medicamento.
* Acción y menú dentro del menú de prescripciones.
* Creación encadenada de ``product.template``, ``product.product`` y
  ``gnuhealth.medicament``.

Dependencias
------------

* ``health``

Pantallas afectadas
-------------------

* Menú de prescripciones de GNU Health.
* Formulario del asistente de alta de medicamento.

Acciones y menús agregados
--------------------------

* Acción ``Crear medicamento``.
* Menú ``Crear medicamento`` debajo de prescripciones.

Campos y comportamiento relevante
---------------------------------

* El asistente pide nombre, componente activo, categoría, concentración,
  presentación, vía, forma y metadatos clínicos.
* La acción genera primero un producto y luego el registro de medicamento.
* Se mantiene comentado el campo ``therapeutic_action`` porque el código
  original ya indicaba que no existe en el formulario estándar.

Limitaciones conocidas
----------------------

* El flujo asume que existe una unidad de medida llamada ``Unit`` o
  ``Unidad``.
* No hay validaciones adicionales sobre duplicados, completitud clínica ni
  consistencia farmacológica.
* El módulo prioriza trazabilidad y documentación por encima de una revisión
  funcional completa del flujo legado.

Estado actual
-------------

* Extraído del módulo monolítico ``health_inpatient_fiuner``.
* Reetiquetado y documentado completamente en español.
* Preparado para instalarse de forma independiente.

Instalación
-----------

1. Copiar el módulo dentro de la ruta de módulos de Tryton.
2. Actualizar la lista de módulos.
3. Instalar ``z_wizard_medication`` desde la administración de módulos.

Validación mínima
-----------------

1. Confirmar que aparece el menú ``Crear medicamento``.
2. Abrir el asistente y verificar que todos los títulos se muestran en español.
3. Crear un medicamento de prueba y comprobar la creación de producto y
   medicamento.
4. Si falla la creación, revisar especialmente la unidad de medida base.

Origen de la extracción
-----------------------

* ``wizard/create_medicament.py``
* ``wizard/create_medicament.xml``
* ``view/create_medicament_start_form.xml``
