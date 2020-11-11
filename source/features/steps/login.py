from behave import given, when, then


@given(u'Я открыл страницу "Входа"')
def open_login_page(context):
    context.browser.get('http://localhost:8000/accounts/login/')


@when(u'Я ввожу текст "{text}" в поле "{name}"')
def enter_text(context, text, name):
    context.browser.find_element_by_name(name).send_keys(text)


@when(u'Я отправляю форму')
def submit_form(context):
    context.browser.find_element_by_id('submit').click()


@then(u'Я должен быть на главной странице')
def should_be_at_main(context):
    assert context.browser.current_url == 'http://localhost:8000/'


@then(u"Я должен быть на странице входа")
def should_be_at_login(context):
    assert context.browser.current_url == 'http://localhost:8000/accounts/login/'


@then(u'Я должен видеть сообщение об ошибке с текстом "{text}"')
def see_error_with_text(context, text):
    error = context.browser.find_elements_by_class_name('error')[0]
    assert error.text == text


@when("Я ввожу следующий текст в следующие поля")
def step_impl(context):
    for row in context.table:
        enter_text(context, row['text'], row['field'])
