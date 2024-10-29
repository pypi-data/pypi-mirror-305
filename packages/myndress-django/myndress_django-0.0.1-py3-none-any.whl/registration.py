def password_validation(password):
    '''
    This method is used to validate a password, it'll check if the password is at least 8 characters long,
    contains at least one digit, one uppercase letter, one lowercase letter and one special character

    :param password: password to validate
    :return: boolean, message
    '''
    special_characters = "!@#$%^&*()-+_"
    errors = []
    if len(password) < 8:
        errors.append("Le mot de passe doit contenir au moins 8 caractères")
    if not any(char.isdigit() for char in password):
        errors.append("Le mot de passe doit contenir au moins un chiffre")
    if not any(char.isupper() for char in password):
        errors.append("Le mot de passe doit contenir au moins une lettre majuscule")
    if not any(char.islower() for char in password):
        errors.append("Le mot de passe doit contenir au moins une lettre minuscule")
    if not any(char in special_characters for char in password):
        errors.append("Le mot de passe doit contenir au moins un caractère spécial: " + special_characters)
    if len(errors) > 0:
        return False, "\n".join(errors)
    return True, "Mot de passe valide"