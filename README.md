# Seguidor de línea 🚁

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![DJI Tello API](https://img.shields.io/badge/DJI_Tello_API-000000?style=for-the-badge&logo=dji&logoColor=white)](https://www.ryzerobotics.com/tello)

Programa desarrollado para el **Mechatronics Grand Prix** en las ediciones FJ2023 y AD2023, en la categoría de seguidor de línea con drones DJI Tello. Este proyecto obtuvo el **2do y 3er lugar** respectivamente.

## 🚀 Instrucciones

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/ErickinSegura/seguidor-de-linea.git
   cd seguidor-de-linea
   ```

2. **Calibración de colores**:
   - Abre el programa `colorpicker.py` para obtener los valores de calibración de los colores de la pista.
   - Copia los valores calibrados y pégalos en el archivo `seguidor.py`, en la variable `hsvVals` (línea 9).

3. **Ejecuta el seguidor de línea**:
   - Una vez calibrado, ejecuta el programa `seguidor.py` para iniciar el seguimiento de la línea con el drone Tello.

## 👥 Autores
- [Erick Segura Sánchez](https://github.com/ErickinSegura)
- [Abdiel Vicencio Antonio](https://github.com/Pezcadoo31)
- [Andrés Daniel Barker Narváez](https://github.com/ADBarNar)

---

### 📝 Notas adicionales
- Asegúrate de tener una buena iluminación en el área de trabajo para una calibración precisa, además que el piso no sea tan reflectante.
- Mantén el drone cargado y verifica que la cámara esté funcionando correctamente antes de ejecutar el programa.
