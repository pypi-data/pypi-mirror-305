import API__Invoke from "../../data/API__Invoke.mjs";

export default class CBR_User_Data {

    target_server             = ''
    url__api__user_profile    = '/api/user-data/user/user-profile'
    url__api__current_session = '/api/user-session/session/current-session'
    auth_header               = 'null'

    constructor() {
        this.setup()
    }

    setup() {
        this.api_invoke = new API__Invoke()
    }

    async current_session() { return await this.api_invoke.invoke_api(this.target_server + this.url__api__current_session ,'GET',null, this.auth_header) }
    async user_profile   () { return await this.api_invoke.invoke_api(this.target_server + this.url__api__user_profile    ,'GET',null, this.auth_header) }

    async login_as_guest_one()  {
        this.login_as_a_guest('6f6df621-42e5-4579-99d8-969e592c1f2b')
    }
    async login_as_guest_two()  {
        this.login_as_a_guest('686a35ef-f78d-4158-a240-11e296cd187a')
    }
    async login_as_guest_three()  {
        this.login_as_a_guest('7a43a0e0-499f-4110-8923-441a7f5028db')
    }
    async login_as_a_guest(guest_id) {
        const api_path = `/api/user-session/guest/login-as-guest?guest_id=${guest_id}`
        await this.api_invoke.invoke_api(api_path)
        location.reload()
    }

    set_mock_responses() {
        this.api_invoke.set_mock_response(this.url__api__current_session, this.mock__api__current_session)
        this.api_invoke.set_mock_response(this.url__api__user_profile   , this.mock__api____user_profile)

        return this
    }

    mock__api__current_session = { data   : { username: 'guest_aabbcc' },
                                   security: {
                                     is_admin_global: false,
                                     is_admin_site: false,
                                     is_blocked: false,
                                     is_customer: false,
                                     is_guest: false,
                                     is_malicious: false,
                                     is_user: false,
                                     is_user_qa: false,
                                     is_suspended: false,
                                     is_suspicious: false
                                   },
                                   session_id: '19ac690e-aaaa-bbbb-cccc-6a1588b47c0d',
                                   user_name: 'guest_aabbcc',
                                   user_id: '9da9279c-aaaa-bbbb-cccc-38cf21a69658',
                                   created__date: '2024-10-24',
                                   created__time: '17:10:01',
                                   timestamp: 1729789801637
                                 }

    mock__api____user_profile = { first_name: 'Guest',
                                  last_name: 'One',
                                  role: 'Board member',
                                  organisation: 'Retail',
                                  sector: 'Food',
                                  size_of_organisation: '10000',
                                  country: 'UK',
                                  linkedin: '',
                                  additional_system_prompt: 'Answer in bullet points'}
}