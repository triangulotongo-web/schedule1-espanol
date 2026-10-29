# Schedule I en español

Traducción no oficial al **español** de [Schedule I](https://store.steampowered.com/app/3164500/Schedule_I/) (TVGS), hecha por fans.

| | |
|---|---|
| **Idioma** | Español (neutro, válido para España y Latinoamérica) |
| **Versión del juego** | **v0.4.7f12** (Steam, build 25796331, Unity 2022.3.62f2 IL2CPP) |
| **Versión de la traducción** | 1.0.0 |
| **Funciona con** | BepInEx 6.0.0-be.791 (IL2CPP) + XUnity.AutoTranslator 5.6.3.1 |

> Si el juego se actualiza, la traducción sigue funcionando: los textos que no cambien salen en español y los nuevos se quedan en inglés hasta que se añadan.

## Qué se traduce

- Menús, ajustes, HUD y avisos
- Mensajes del teléfono y diálogos de los personajes
- Misiones, objetivos y tutoriales
- Nombres y descripciones de objetos, efectos, rangos y empleados

En total son **3.266 frases fijas** y **47 patrones** para frases que el juego monta con datos variables (nombres, cantidades, rangos). Los nombres propios (personajes, barrios, tiendas, cepas) se quedan como en el original.

## Instalación

1. Descarga **BepInEx 6 para Unity IL2CPP x64** ([BepInEx-Unity.IL2CPP-win-x64-6.0.0-be.791](https://builds.bepinex.dev/projects/bepinex_be)) y descomprímelo en la carpeta del juego:
   `C:\Program Files (x86)\Steam\steamapps\common\Schedule I\`
2. Descarga **XUnity.AutoTranslator-BepInEx-IL2CPP-5.6.3.1.zip** desde [sus versiones en GitHub](https://github.com/bbepis/XUnity.AutoTranslator/releases) y descomprímelo también en la carpeta del juego.
3. Copia el contenido de este repositorio:
   - `config/AutoTranslatorConfig.ini` → `Schedule I\BepInEx\config\`
   - la carpeta `Translation` → `Schedule I\BepInEx\` (debe quedar `BepInEx\Translation\es\Text\ScheduleI_es.txt`)
4. Abre el juego desde Steam. **La primera vez tarda varios minutos** en arrancar porque BepInEx prepara sus archivos; después arranca normal.

La configuración deja la traducción automática por internet **desactivada**: solo se usan los textos de este repositorio y el mod no envía nada a ningún servicio.

### Desinstalar

Borra de la carpeta del juego `BepInEx`, `dotnet`, `winhttp.dll`, `doorstop_config.ini` y `changelog.txt`.

## Atajos del mod

- **Alt + T**: alterna entre español e inglés (útil para comparar).
- **Alt + R**: recarga los archivos de traducción sin cerrar el juego.

## Cómo se hizo

Los textos se sacaron de los archivos del propio juego con los scripts de [`tools/`](tools):

- `extract.py`: lee los MonoBehaviour de los `.assets` y niveles con UnityPy y los literales de `global-metadata.dat`.
- `filter.py` y `filter2.py`: descartan identificadores, logs y mensajes técnicos.
- `merge.py`: une los lotes traducidos y comprueba el formato de XUnity y que los patrones sean expresiones regulares válidas.

Este repositorio **no incluye ningún archivo del juego**, solo las traducciones y la configuración del mod.

## Corregir o añadir textos

Los archivos de `Translation/es/Text/` tienen una línea por texto:

```
Texto original=Texto traducido
r:"^Unlocks at (.+)$"=Se desbloquea en $1
```

Dentro de cada lado, `=` se escribe `\=` y un salto de línea `\n`. Si ves algo mal traducido o en inglés, abre un *issue* con una captura o manda un *pull request*.

## Aviso legal

Proyecto de fans sin relación con TVGS ni con los autores de Schedule I. Schedule I y su contenido pertenecen a sus dueños. Necesitas tener el juego original comprado en Steam.
