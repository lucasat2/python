def calcular_dano_combo(*golpes):
  dano_total = 0
  combo_nome = None

  # Dicionário de danos
  danos = {'S': 10, 'C': 20, 'E': 50}

  # Calcular dano base
  for golpe in golpes:
    dano_total += danos.get(golpe, 0)

  # Verificar combos
  golpes_str = ''.join(golpes)
  if 'S,S,C' in golpes_str:
    dano_total += int(dano_total * 0.30)
    combo_nome = 'Combo Básico'
  elif 'S,C,C,E' in golpes_str:
    dano_total += int(dano_total * 0.50)
    combo_nome = 'Combo Avançado'
  elif 'E,E,S' in golpes_str:
    dano_total += dano_total
    combo_nome = 'Combo Secreto'

  return dano_total, combo_nome

# Exemplo de uso
dano, combo = calcular_dano_combo('S', 'S', 'C', 'E')
print(f"Dano Total: {dano}, Combo: {combo}")