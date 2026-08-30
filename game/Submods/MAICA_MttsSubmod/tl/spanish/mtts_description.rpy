translate spanish python:

    import mtts_provider_manager as mpm

    mpm.MTTSProviderManager._isfailedresponse.update(
        {
            "name": "ERROR: No se pudo obtener la información del nodo.",
            "description": "Consulta el registro de actualizaciones para ver el estado actual del servicio, o revisa submod_log.log para conocer el motivo del fallo.",
            "isOfficial": False,
            "portalPage": "https://forum.monika.love/d/3954",
            "servingModel": "Consulta el registro de actualizaciones para ver el estado actual del servicio, o revisa submod_log.log para conocer el motivo del fallo.",
            "modelLink": "",
            "wsInterface": "wss://maicadev.monika.love/websocket",
            "httpInterface": "https://maicadev.monika.love/api"
        }
    )
    mpm.MTTSProviderManager._fakelocalprovider.update(
        {
            "name": "Despliegue local",
            "description": "Selecciona este nodo cuando dispongas de un despliegue local operativo.",
            "isOfficial": False,
            "portalPage": "https://github.com/PencilMario/MAICA",
            "servingModel": "None",
            "modelLink": "",
            "wsInterface": "ws://127.0.0.1:5000",
            "httpInterface": "http://127.0.0.1:6000",
        }
    )
