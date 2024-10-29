import Web_Component    from '../../core/Web_Component.mjs';
import CSS__Cards      from '../../css/CSS__Cards.mjs';
import CSS__Typography from '../../css/CSS__Typography.mjs';
import API__Invoke     from '../../data/API__Invoke.mjs';
import Div             from '../../core/Div.mjs';
import H               from '../../core/H.mjs';
import CSS__Grid       from "../../css/grid/CSS__Grid.mjs";

export default class WebC__Athena__Welcome extends Web_Component {
    load_attributes() {
        new CSS__Grid      (this).apply_framework()
        new CSS__Cards     (this).apply_framework()
        new CSS__Typography(this).apply_framework()
        this.api_invoke = new API__Invoke()
        this.welcome_message = ''
    }

    async connectedCallback() {
        super.connectedCallback()
        await this.generate_welcome()
        this.render()
    }

    async fetch_user_data() {
        try {
            return await this.api_invoke.invoke_api('/api/user-data/user/user-profile', 'GET')
        } catch (error) {
            console.error('Error fetching user data:', error)
            return null
        }
    }

    async generate_welcome() {
        const user_data     = await this.fetch_user_data()
        const user_prompt   = "Generate a one-paragraph personalized welcome message for this user, mentioning their role and sector. Keep it professional but warm."
        const system_prompt = `Please customize the welcome message for this user based on their profile: ${JSON.stringify(user_data)}`

        if (!user_data) return

        const payload = {
            chat_thread_id: this.random_uuid(),
            model       : "gpt-4o",
            temperature: 0,
            user_prompt: user_prompt,
            images: [],
            system_prompts: [system_prompt],
            histories: [],
            user_data: { session_id: this.random_uuid() },
            stream: true
        }

        const path = '/api/open_ai/prompt_with_system__stream'
        try {
            const response = await fetch(path, {method: 'POST', headers: { 'Accept': 'application/json',  'Content-Type': 'application/json' },
                                                body : JSON.stringify(payload) })
            const reader = response.body.getReader();                     // Handling the stream
            const decoder = new TextDecoder('utf-8');
            let { value, done } = await reader.read();
            let message = '';
            while (!done) {
                message += decoder.decode(value, { stream: true });
                ({ value, done } = await reader.read());
                this.welcome_message = message
                this.render()
            }
            message += decoder.decode();
            this.welcome_message = message
            this.render()

        } catch (error) {
            console.error('Error generating welcome:', error)
        }
    }

    render() {
        const card = new Div({ class: 'card h-100 m-1' })
        const body = new Div({ class: 'card-body' })
        const title = new H({ level: 3, class: 'card-title mb-3', value: 'Welcome' })
        const content = new Div({ class: 'card-text', value: this.welcome_message })

        body.add_elements(title, content)
        card.add_element(body)

        this.set_inner_html(card.html())
    }
}

WebC__Athena__Welcome.define()