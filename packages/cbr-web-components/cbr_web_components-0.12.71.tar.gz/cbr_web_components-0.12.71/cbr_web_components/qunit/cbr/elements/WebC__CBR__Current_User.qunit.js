import Web_Component            from "../../../js/core/Web_Component.mjs";
import WebC__CBR__Current_User  from "../../../js/cbr/elements/WebC__CBR__Current_User.mjs";
import WebC__Target_Div         from "../../../js/utils/WebC__Target_Div.mjs";

QUnit.module('WebC__CBR__Current_User', function(hooks) {

    let webc_cbr_current_user
    let target_div

    hooks.before(async (assert) => {
        target_div            = WebC__Target_Div.add_to_body().build({width: "50%"})
        webc_cbr_current_user = WebC__CBR__Current_User.create()
        webc_cbr_current_user.cbr_user_data.set_mock_responses()
        await target_div.appendChild(webc_cbr_current_user)
        await webc_cbr_current_user.wait_for_event('build-complete')
    });



    hooks.after((assert) => {
        target_div.remove()
        webc_cbr_current_user.remove()
    })

    QUnit.test('constructor', (assert) =>  {
        assert.equal(webc_cbr_current_user.constructor.name, 'WebC__CBR__Current_User')
        assert.ok   (webc_cbr_current_user instanceof Web_Component)
        assert.ok   (WebC__CBR__Current_User.prototype instanceof Web_Component);
        assert.equal(webc_cbr_current_user.cbr_user_data.url__api__user_profile      , '/api/user-data/user/user-profile'         )
        assert.equal(webc_cbr_current_user.cbr_user_data.url__api__current_session   , '/api/user-session/session/current-session')
    })

    QUnit.test('build', (assert) =>  {
        //console.log(webc_cbr_current_user.inner_html())
        assert.ok(1)
    })


})