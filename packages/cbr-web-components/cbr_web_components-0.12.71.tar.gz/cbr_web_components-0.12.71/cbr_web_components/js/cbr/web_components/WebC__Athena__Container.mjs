import Web_Component    from '../../core/Web_Component.mjs';
import Layout          from '../../css/grid/Layout.mjs';
import CSS__Grid       from '../../css/grid/CSS__Grid.mjs';
import CSS__Typography from '../../css/CSS__Typography.mjs';

export default class WebC__Athena__Container extends Web_Component {
    load_attributes() {
        new CSS__Grid      (this).apply_framework()
        new CSS__Typography(this).apply_framework()
        this.channel = this.getAttribute('channel') || `athena_${this.random_id()}`
    }

    render() {
        // Main layout container
        const layout = new Layout({
            id: 'athena-page',
            class: 'h-100pc d-flex flex-column'
        })

        // Banner row
        const row_banner = layout.add_row({ id: 'athena-row',  class: 'm-1' })

        row_banner.add_col({id: 'athena-banner',  class: 'col-12' })
                  .add_tag({ tag: 'webc-athena-banner'})

        // Content row
        const row_content = layout.add_row({ class: 'flex-fill m-1' })

        // Chat column
        row_content.add_col({class: 'col-9'})
                    .add_tag({ tag            : 'chatbot-openai',
                               initial_message: 'Hello, I am Athena. How can I help you?',
                               channel  : this.channel    ,
                               edit_mode: 'false'         ,
                               name     : 'Athena'        ,
                               url      : '/api/open_ai/prompt_with_system__stream'})
        row_content .add_col({ class    : 'col-3', id: 'examples-col'})
                    .add_tag({ tag      : 'webc-athena-examples'      ,
                               channel  : this.channel               })

        this.set_inner_html(layout.html())
    }
}

WebC__Athena__Container.define()