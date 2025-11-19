from behave import *

from python_gherkin.dossier_data import DossierStatus
from python_gherkin.dossier_service import create_dossier, read_submitted_dossiers, submit_dossier, \
    get_dossier, update_summary


@given(u'un dossier rempli par un utilisateur A')
def step_impl(context):
    context.dossier_id = create_dossier("AnySummary")


@when(u'L\'utilisateur A soumet son dossier')
def step_impl(context):
    try:
        submit_dossier(context.dossier_id)
    except Exception as e:
        context.exception = e


@then(u'Le dossier est visible dans la liste des dossiers à valider pour l\'utilisateur B')
def step_impl(context):
    submitted_dossiers = read_submitted_dossiers()
    assert any(dossier for dossier in submitted_dossiers if dossier.id == context.dossier_id and dossier.status == DossierStatus.SUBMITTED)

@given(u'un dossier soumis par l\'utilisateur A')
def step_impl(context):
    try:
        submit_dossier(context.dossier_id)
    except Exception as e:
        context.exception = e


@then(u'une erreur survient')
def step_impl(context):
    assert hasattr(context, "exception")


@when(u'L\'utilisateur A modifie le sommaire du dossier avec "{given_summary}"')
def step_impl(context, given_summary: str):
    try:
        update_summary(context.dossier_id, given_summary)
    except Exception as e:
        context.exception = e


@then(u'Le sommaire du dossier est "{expected_summary}"')
def step_impl(context, expected_summary):
    dossier = get_dossier(context.dossier_id)
    assert dossier.summary == expected_summary
