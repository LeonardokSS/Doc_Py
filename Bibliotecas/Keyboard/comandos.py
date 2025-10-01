import keyboard  # Biblioteca para automação e captura de teclado

# Ações com teclas
keyboard.press('a')  # Pressiona a tecla 'a'
keyboard.release('a')  # Solta a tecla 'a'
keyboard.write("Olá, mundo!", delay=0.1)  # Digita o texto
keyboard.send('ctrl+c')  # Pressiona combinação de teclas

# Eventos de tecla
keyboard.is_pressed('shift')  # Verifica se 'shift' está pressionado
keyboard.read_key()  # Retorna a próxima tecla pressionada
keyboard.read_event()  # Retorna o próximo evento de teclado
keyboard.record(until='esc')  # Grava eventos até 'esc'
keyboard.play([], speed_factor=1.0)  # Reproduz eventos gravados

# Atalhos e hotkeys
keyboard.add_hotkey('ctrl+alt+n', lambda: print("Hotkey ativada!"))  # Define um hotkey
keyboard.remove_hotkey('ctrl+alt+n')  # Remove hotkey específico
keyboard.clear_all_hotkeys()  # Remove todos os hotkeys

# Bloqueio e hooks
keyboard.block_key('esc')  # Bloqueia tecla
keyboard.unblock_key('esc')  # Desbloqueia tecla
keyboard.hook(lambda e: print(e.name, e.event_type))  # Hook global de teclado
keyboard.unhook(lambda e: print(e.name, e.event_type))  # Remove hook
keyboard.hook_key('a', lambda e: print("Tecla 'a' pressionada!"))  # Hook para tecla específica

# Listar teclas e códigos
keyboard.all_modifiers  # Lista todas as teclas modificadoras
keyboard.all_modifiers_set()  # Retorna modificadoras pressionadas
keyboard.key_to_scan_codes('a')  # Retorna códigos de varredura
keyboard.is_modifier('shift')  # Verifica se é tecla modificadora

# Exemplos práticos
keyboard.wait('ctrl+c')  # Espera até Ctrl+C para encerrar
