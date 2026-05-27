


graph TD
    A([Inicio]) --> B[Definir salud_jefe = 100<br>Definir energia = 50]
    B --> C{¿Quedan ataques<br>en la lista?}
    C -- Sí --> D[Obtener siguiente ataque]
    C -- No --> R{¿salud_jefe <= 0?}

    D --> E[Try: Extraer tipo en indice 0<br>y daño en indice 1]
    E --> F{¿Ocurrió un Error?<br>ej. Faltan datos}
    F -- Sí Catch --> G[Mostrar 'Ataque fallido'<br>Ignorar y continuar]
    F -- No --> H{¿Daño > 0?}

    G --> C
    H -- No --> C
    H -- Sí --> J{¿Tipo == 'Especial'?}

    J -- Sí --> K{¿energia >= 20?}
    K -- Sí --> L[salud_jefe -= Daño * 2<br>energia -= 20]
    K -- No --> M[Mostrar 'Sin energía']
    M --> C

    J -- No --> N[salud_jefe -= Daño]

    L --> O
    N --> O{¿salud_jefe <= 0?}

    O -- Sí --> P[Mostrar '¡Jefe Derrotado!']
    P --> Q([Fin del Programa - Romper Ciclo])
    O -- No --> C

    R -- Sí --> P
    R -- No --> S[Mostrar 'El jefe sobrevive']
    S --> T([Fin del Programa])





     print("Ataque fallido")
        continue

    if dano <= 0:
        continue

    if tipo == "Especial":

        if energia >= 20:
            salud_jefe -= dano * 2
            energia -= 20

            print(f"Ataque especial realizado. "
                  f"Daño: {dano * 2}")

        else:
            print("Sin energía")
            continue

    else:
        salud_jefe -= dano

        print(f"Ataque normal realizado. "
              f"Daño: {dano}")

    print(f"Salud restante del jefe: {salud_jefe}")
    print(f"Energía restante: {energia}")
    print("-" * 40)

    if salud_jefe <= 0:
        print("¡Jefe derrotado!")
        break

if salud_jefe > 0:
    print("El jefe sobrevive")