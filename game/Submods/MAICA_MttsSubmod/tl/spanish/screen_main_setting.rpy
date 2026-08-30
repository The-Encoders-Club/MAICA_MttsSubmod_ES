translate spanish strings:

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:64
    old "Connection and security"
    new "Conexión y seguridad"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:68
    old "Current provider: [provider_name]"
    new "Proveedor actual: [provider_name]"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:70
    old "Set server node"
    new "Configurar nodo del servidor"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:74
    old "Not logged in"
    new "No has iniciado sesión"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:75
    old "Current user: [user_disp]"
    new "Usuario actual: [user_disp]"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:77
    old "To change or log out of your account, log out from the Submods screen.\n* To change account information or password, visit the registration website"
    new "Para cambiar de cuenta o cerrarla, cierra sesión desde la pantalla de Submods.\n* Para modificar la información de la cuenta o la contraseña, visita el sitio web de registro"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:82
    old "Behavior and performance"
    new "Comportamiento y rendimiento"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:87
    old "Enable MTTS: [persistent.mtts.get('enabled')]"
    new "Habilitar MTTS: [persistent.mtts.get('enabled')]"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:89
    old "Enable to generate and play TTS audio."
    new "Habilita para generar y reproducir audio TTS."

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:95
    old "! MTTS not unlocked, enabling will not take effect"
    new "¡MTTS no está desbloqueado, habilitarlo no tendrá efecto!"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:101
    old "Enable to generate and play TTS audio.\n! MTTS not unlocked, enabling will not take effect"
    new "Habilita para generar y reproducir audio TTS.\n! MTTS no está desbloqueado, habilitarlo no tendrá efecto"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:104
    old "TTS audio volume"
    new "Volumen de audio TTS"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:105
    old "TTS volume"
    new "Volumen TTS"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:107
    old "Skip current sentence if response time exceeds.\n* Do not set this too low"
    new "Omitir la frase actual si el tiempo de respuesta supera el límite.\n* No establezcas este valor demasiado bajo"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:108
    old "Generation timeout (s)"
    new "Límite de espera de generación (s)"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:111
    old "Tools and features"
    new "Herramientas y funciones"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:115
    old "Display props when enabled: [persistent.mtts.get('acs_enabled')]"
    new "Mostrar accesorios al habilitar: [persistent.mtts.get('acs_enabled')]"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:117
    old "Enable or disable MTTS microphone when using TTS.\n* MTTS headset not included since it's normal acs"
    new "Habilita o deshabilita el micrófono MTTS al usar TTS.\n* Los auriculares MTTS no están incluidos ya que son un accesorio normal"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:131
    old "Replace player name: [persistent.mtts.get('replace_playername')]"
    new "Reemplazar nombre del jugador: [persistent.mtts.get('replace_playername')]"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:133
    old "Enable or disable player name replacement in speech generation.\n! Implemented directly through regex. Do not use if your in-game name commonly appears in unrelated context"
    new "Habilita o deshabilita el reemplazo del nombre del jugador en la generación de voz.\n! Implementado mediante expresiones regulares. No usar si tu nombre en el juego aparece en contextos no relacionados"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:138
    old "Replace to: [replacement]"
    new "Reemplazar por: [replacement]"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:140
    old "Configure your spoken name.\n* Leave empty to not pronounce, but may lead to behaviour issue"
    new "Configura el nombre para pronunciar.\n* Déjalo vacío para no pronunciar nada, pero puede causar fallos de entonación"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:153
    old "Show status HUD: [persistent.mtts.get('ministathud')]"
    new "Mostrar HUD de estado: [persistent.mtts.get('ministathud')]"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:155
    old "Enable or disable MTTS status widget"
    new "Habilita o deshabilita el widget de estado de MTTS"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:159
    old "Compatible position left: [persistent.mtts.get('drift_statshud_l')]"
    new "Posición compatible izquierda: [persistent.mtts.get('drift_statshud_l')]"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:161
    old "Enable or disable offseting status HUD to avoid possible conflict with other submods.\n* MTTS status HUD occupies bottom left of screen space by default\n* MTTS status HUD will be closer to central Y on left side if enabled"
    new "Habilita o deshabilita el desplazamiento del HUD de estado para evitar conflictos con otros submods.\n* El HUD de MTTS ocupa la parte inferior izquierda de la pantalla por defecto\n* Si se habilita, se situará más cerca del centro vertical izquierdo"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:165
    old "Compatible position right: [persistent.mtts.get('drift_statshud_r')]"
    new "Posición compatible derecha: [persistent.mtts.get('drift_statshud_r')]"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:167
    old "Enable or disable offseting status HUD to avoid possible conflict with other submods.\n* MTTS status HUD occupies top right of screen space if console (like MAICA) displayed\n* MTTS status HUD will be closer to central Y on right side if enabled"
    new "Habilita o deshabilita el desplazamiento del HUD de estado para evitar conflictos con otros submods.\n* El HUD de MTTS ocupa la parte superior derecha si la consola (como MAICA) está visible\n* Si se habilita, se situará más cerca del centro vertical derecho"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:178
    old "MTTS local cache to reduce resource consumption and latency.\n* Flush cache to apply new performance on model change\n! Do {color=#FF0000}NOT{/color} flush unless you know what you're doing"
    new "Caché local de MTTS para reducir el consumo de recursos y la latencia.\n* Vacía el caché para aplicar nuevos ajustes si cambias de modelo\n! {color=#FF0000}NO{/color} vacíes el caché a menos que sepas lo que haces"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:183
    old "Current cache size: [store.mtts.mtts_instance.cache.cache_size]MB"
    new "Tamaño actual de la caché: [store.mtts.mtts_instance.cache.cache_size]MB"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:190
    old "{color=#FF0000}Flush cache{/color}"
    new "{color=#FF0000}Vaciar caché{/color}"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:205
    old "Enable customized advanced parameters: [persistent.mtts.get('use_custom_model_config', False)]"
    new "Habilitar parámetros avanzados personalizados: [persistent.mtts.get('use_custom_model_config', False)]"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:207
    old "Advanced parameters could significantly affect the model's performance.\n* The default is already the best field-tested config, so it's not suggested to enable this"
    new "Los parámetros avanzados pueden afectar significativamente el rendimiento del modelo.\n* La configuración por defecto ya es la óptima comprobada, no se sugiere habilitar esto"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:212
    old "Set advanced parameters"
    new "Configurar parámetros avanzados"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:216
    old "! Active advanced parameters will disable remote cache, demanding per-request inference and transferring\n! This could cause massive extra cost on both server and client side, do consider carefully\n* Flush local cache to apply new performance"
    new "¡Los parámetros avanzados activos desactivarán la caché remota, requiriendo inferencia y transferencia por cada petición!\n¡Esto podría generar un gran coste adicional en el servidor y en tu tráfico de datos, piénsalo bien!\n* Vacía la caché local para aplicar el nuevo rendimiento"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:228
    old "Expand performance monitor"
    new "Expandir monitor de rendimiento"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:228
    old "Collapse performance monitor"
    new "Contraer monitor de rendimiento"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:230
    old "Show/hide server performance metrics"
    new "Mostrar/ocultar métricas de rendimiento del servidor"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:246
    old "MTTS: Settings saved"
    new "MTTS: Ajustes guardados"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:251
    old "Discard changes"
    new "Descartar cambios"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:252
    old "MTTS: Settings discarded"
    new "MTTS: Cambios descartados"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:258
    old "MTTS: Settings reset"
    new "MTTS: Ajustes restablecidos"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:277
    old "Flush cache"
    new "Vaciar caché"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:279
    old "Do {color=#FF0000}NOT{/color} flush unless you know what you're doing, which could cause massive extra cost on both server and client side"
    new "{color=#FF0000}NO{/color} vacíes la caché a menos que sepas lo que haces, ya que podría causar un gran coste adicional de recursos en el servidor y en el cliente"

    # game/Submods/MAICA_MttsSubmod/screen_main_setting.rpy:282
    old "Please confirm you understand what this means, or instructed by a MAICA technician"
    new "Por favor confirma que comprendes lo que esto significa, o que has sido instruido por un técnico de MAICA"
