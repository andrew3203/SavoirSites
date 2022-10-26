def get_html_msg(contact):
    text = f"Новый контакт: <u>{contact.site}</u><br><br>" \
        f"Имя: <b>{contact.name}</b><br>" \
        f"Телефон: <b>{contact.phone}</b><br>" \
        f"Почта: <b>{contact.email}</b><br><br>" \
        f"Объект: <b>{contact.complex}</b>" 
    return text

def get_text_msg(contact):
    text = f"Новый контакт: {contact.site}" + "\n\n" \
        f"Имя: {contact.name}" + "\n\n"  \
        f"Телефон: {contact.phone}" + "\n\n"  \
        f"Почта: {contact.email}" + "\n\n"  \
        f"Объект: {contact.complex}" 
    return text