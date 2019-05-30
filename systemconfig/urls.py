from django.conf.urls import url, include
from systemconfig.views import *

app_name = 'systemconfig'

urlpatterns = [
    url(r'^admin/', include([

        url(r'^addcity/', citytown.addCityTown.as_view(), name='city.admin.addcity'),
        url(r'^savecity/', citytown.saveCityTown.as_view(), name='city.admin.savecity'),
        url(r'^editcity/(?P<edit_id>.+)', citytown.editCityTown.as_view(), name='city.admin.editcity'),
        url(r'^updatecity/', citytown.updateCityTown.as_view(), name='city.admin.updatecity'),

        url(r'^addcountry/', country.addCountry.as_view(), name='country.admin.addcity'),
        url(r'^savecountry', country.saveCountry.as_view(), name='country.admin.savecountry'),
        url(r'^editcountry/(?P<edit_id>.+)', country.editCountry.as_view(), name='country.admin.editcountry'),
        url(r'^updatecountry/', country.updateCountry.as_view(), name='country.admin.updatecountry'),

        url(r'^addlanguage/', language.addLanguage.as_view(), name='language.admin.addcity'),
        url(r'^savelanguage/', language.saveLanguage.as_view(), name='language.admin.savelanguage'),
        url(r'^editlanguage/(?P<edit_id>.+)', language.editLanguage.as_view(), name='language.admin.editlanguage'),
        url(r'^updatelanguage/', language.updateLanguage.as_view(), name='language.admin.updatelanguage'),

        url(r'^addnationality/', nationality.addNationality.as_view(), name='nationality.admin.addcity'),
        url(r'^savenationality/', nationality.saveNationality.as_view(), name='nationality.admin.savenationality'),
        url(r'^editnationality/(?P<edit_id>.+)', nationality.editNationality.as_view(),
            name='nationality.admin.editnationality'),
        url(r'^updatenationality/', nationality.updateNationality.as_view(),
            name='nationality.admin.updatenationality'),

        url(r'^addoccupation/', occupation.addOccupation.as_view(), name='occupation.admin.addcity'),
        url(r'^saveoccupation', occupation.saveOccupation.as_view(), name='occupation.admin.saveoccupation'),
        url(r'^editoccupation/(?P<edit_id>.+)', occupation.editOccupation.as_view(),
            name='occupation.admin.editoccupation'),
        url(r'^updateoccupation/', occupation.updateOccupation.as_view(), name='occupation.admin.updateoccupation'),

        url(r'^addrelationship/', relationship.addRelationship.as_view(), name='relationship.admin.addrelationship'),
        url(r'^saverelationship', relationship.saveRelationship.as_view(), name='relationship.admin.saverelationship'),
        url(r'^editrelationship/(?P<edit_id>.+)', relationship.editRelationship.as_view(),
            name='relationship.admin.editrelationship'),
        url(r'^updaterelationship/', relationship.updateRelationship.as_view(),
            name='relationship.admin.updaterelationship'),

        url(r'^addreligion/', religion.addReligion.as_view(), name='religion.admin.addreligion'),
        url(r'^savereligion/', religion.saveReligion.as_view(), name='religion.admin.savereligion'),
        url(r'^editreligion/(?P<edit_id>.+)', religion.editReligion.as_view(), name='religion.admin.editreligion'),
        url(r'^updatereligion/', religion.updateReligion.as_view(), name='religion.admin.updatereligion'),

        url(r'^addstate/', state.addState.as_view(), name='state.admin.addstate'),
        url(r'^savestate/', state.saveState.as_view(), name='state.admin.savestate'),
        url(r'^editstate/(?P<edit_id>.+)', state.editState.as_view(), name='state.admin.editstate'),
        url(r'^updatestate/', state.updateState.as_view(), name='state.admin.updatestate'),

        url(r'^addorganization/', organization.addOrganization.as_view(), name='organization.admin.addorganization'),
        url(r'^saveorganization/', organization.saveOrganization.as_view(), name='organization.admin.saveorganization'),
        url(r'^editorganization/(?P<edit_id>.+)', organization.editOrganization.as_view(),
            name='organization.admin.editorganization'),
        url(r'^updateorganization/', organization.updateOrganization.as_view(),
            name='organization.admin.updateorganization'),

        url(r'^addsmsconfig/', smsconfig.addSmsConfig.as_view(), name='smsconfig.admin.addsmsconfig'),
        url(r'^savesmsconfig/', smsconfig.saveSmsConfig.as_view(), name='smsconfig.admin.savesmsconfig'),
        url(r'^editsmsconfig/(?P<edit_id>.+)', smsconfig.editSmsConfig.as_view(), name='smsconfig.admin.editsmsconfig'),
        url(r'^updatesmsconfig/', smsconfig.updateSmsConfig.as_view(), name='smsconfig.admin.updatesmsconfig'),

        url(r'^addemailconfig/', emailconfig.addEmailConfig.as_view(), name='emailconfig.admin.addemailconfig'),
        url(r'^saveemailconfig/', emailconfig.saveEmailConfig.as_view(), name='emailconfig.admin.saveemailconfig'),
        url(r'^editemailconfig/(?P<edit_id>.+)', emailconfig.editEmailConfig.as_view(),
            name='emailconfig.admin.editemailconfig'),
        url(r'^updateemailconfig/', emailconfig.updateEmailConfig.as_view(),
            name='emailconfig.admin.updateemailconfig'),

    ]))
]
