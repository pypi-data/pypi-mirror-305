import CBR_User_Data    from "../utils/CBR_User_Data.mjs";
import Web_Component    from "../../core/Web_Component.mjs";
import Div              from "../../core/Div.mjs";
import Pre              from "../../core/Pre.mjs";
import Text             from "../../core/Text.mjs";
import Svg__Icons       from "../../core/Svg__Icons.mjs";

export default class WebC__CBR__Current_User extends Web_Component {

    cbr_user_data = new CBR_User_Data()

    async connectedCallback() {
        super.connectedCallback()
        this.setup()
        await this.build()
        this.raise_event('build-complete')
    }
    setup() {
        window.cbr_user_data             = this.cbr_user_data
    }
    async build() {
        try {
            const user_profile            = await this.cbr_user_data.user_profile()
            const svg_screenshot          = new Svg__Icons().icon('user_profile')
            const svg_picture_as_pdf      = new Svg__Icons().icon('picture_as_pdf')
            const svg_screenshot_monitor  = new Svg__Icons().icon('screenshot_monitor')
            const div_current_user        = new Div({class:'current_user'})
            const text_user_profile       = new Text({level:1, value:'User Profile'})
            const pre_user_profile        = new Pre({value: JSON.stringify(user_profile, null, 2)})

            div_current_user.add_elements(svg_picture_as_pdf, svg_screenshot_monitor, svg_screenshot)
            div_current_user.add_elements(text_user_profile,pre_user_profile)
            //div_current_user.add_elements(h2_user_profile)
            this.set_inner_html(div_current_user.html())
        } catch (error) {
            console.error(error)
            this.set_inner_html(error)
        }

    }
}

WebC__CBR__Current_User.define()