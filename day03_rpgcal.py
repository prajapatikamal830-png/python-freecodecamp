full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'

    if name == '':
        return 'The character should have a name' 

    if len(name) > 10:
        return 'The character name is too long'

    if ' ' in name:
        return 'The character name should not contain spaces' 

    if not all(isinstance(stats, int) for stats in (strength, intelligence, charisma)):
        return 'All stats should be integers'

    if any(stats < 1 for stats in (strength, intelligence, charisma)):
        return 'All stats should be no less than 1'
       
    if any(stats > 4 for stats in (strength, intelligence, charisma)):
        return 'All stats should be no more than 4'

    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    
    # dots creation
    str_line = full_dot * strength + empty_dot * (10 - strength)
    int_line = full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_line = full_dot * charisma + empty_dot * (10 - charisma)

    return (
        f"{name}\n"
        f"STR {str_line}\n"
        f"INT {int_line}\n"
        f"CHA {cha_line}"
    )
print(create_character('ren', 4, 2, 1))