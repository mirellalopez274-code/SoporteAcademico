# Sistema de Soporte Académico

## Descripción
Programa de consola desarrollado en Python para registrar y gestionar solicitudes de estudiantes del módulo de Soporte Académico.

## Objetivo
Registrar solicitudes, validar los datos ingresados y asignar una prioridad de atención mediante funciones y modularidad.

## Lenguaje utilizado
Python

## Funcionalidades
- Registrar solicitudes de estudiantes.
- Validar el código del estudiante.
- Validar textos obligatorios.
- Validar el tipo de consulta.
- Asignar prioridad de atención.
- Mostrar el resumen de una solicitud.
- Mostrar las solicitudes registradas.

## Tipos de consulta
- Matrícula
- Pagos
- Constancia
- Plataforma
- Otro

## Prioridades
- Matrícula y pagos: ALTA
- Constancia, plataforma y otro: BAJA
## Funciones y requisitos

- mostrar_menu(): muestra el menú principal del sistema. Cumple el Req. 4.
- asignar_prioridad(tipo): determina la prioridad de la solicitud según el tipo de consulta. Cumple el Req. 5.
- validar_texto(texto): valida que los campos de texto obligatorios no estén vacíos. Cumple el Req. 6.
- mostrar_resumen(solicitud): muestra los datos de una solicitud registrada. Cumple el Req. 7.
- validar_codigo(codigo): valida que el código del estudiante no esté vacío y tenga la longitud mínima establecida. Apoya el Req. 2.
- validar_tipo_consulta(tipo): verifica que el tipo de consulta sea válido. Apoya el Req. 3.
- registrar_solicitud(solicitudes): recibe la lista mediante parámetros y registra una solicitud. Apoya los Req. 1 y 8.
- mostrar_solicitudes(solicitudes): muestra las solicitudes almacenadas y permite comprobar el registro de múltiples solicitudes. Apoya los Req. 9 y 10.
- main(): controla el flujo principal del programa y mantiene las variables principales dentro de su alcance.
## Pruebas realizadas

| Caso de prueba | Resultado |
|---|---|
| Datos válidos | Correcto |
| Código vacío | Correcto |
| Tipo incorrecto | Correcto |
| Prioridad alta | Correcto |
| Prioridad baja | Correcto |

Las pruebas fueron ejecutadas en el programa para comprobar las
validaciones y la asignación de prioridades.