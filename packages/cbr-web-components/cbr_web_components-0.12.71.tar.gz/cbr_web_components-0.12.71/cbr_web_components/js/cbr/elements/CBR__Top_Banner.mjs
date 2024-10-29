import Div  from "../../core/Div.mjs"
import Icon from "../../css/icons/Icon.mjs"
import Img  from "../../core/Img.mjs"

export default class Top_Banner extends Div {
    constructor({username = 'guest', id, ...kwargs}={}) {
        kwargs.class = `top-banner ${kwargs.class || ''}`
        super({id, ...kwargs})

        const menuIcon         = new Icon({ class: 'menu-icon icon-lg'  , icon: 'menu'                                       })    // Hamburger menu
        const userContainer    = new Div ({ class: 'user-container'                                                          })    // User container (right side)
        const userImgContainer = new Div ({ class: 'user-img-container'                                                      })    // User profile image
        const userImg          = new Img ({ class: 'user-img img-circle', src: '/assets/cbr/account-circle.svg',  alt: 'User'})
        const userText         = new Div({ class: 'user-text'           ,  value: username                                   }) // Username
        userImgContainer.add_element(userImg)
        userContainer   .add_elements(userImgContainer, userText)
        this.add_elements(menuIcon, userContainer)
    }

    static css_rules() {
        return {
            ".top-banner": {
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                padding: "0 1rem",
                height: "100%",
                backgroundColor: "#1e88e5",
                color: "#ffffff",
            },

            ".menu-icon": {
                color: "#ffffff",
                cursor: "pointer",
                fontSize: "1.75rem",
                padding: "0.5rem",
                marginLeft: "-0.5rem"
            },

            ".user-container": {
                display: "flex",
                alignItems: "center",
                gap: "0.75rem"
            },

            ".user-img-container": {
                width: "32px",
                height: "32px",
                borderRadius: "50%",
                overflow: "hidden",
                backgroundColor: "#ffffff"
            },

            ".user-img": {
                width: "100%",
                height: "100%",
                objectFit: "cover"
            },

            ".user-text": {
                fontSize: "1.2rem",
                fontWeight: "400",
                letterSpacing: "0.25px"
            },

            // Hover states
            ".menu-icon:hover": {
                backgroundColor: "rgba(255, 255, 255, 0.1)",
                borderRadius: "4px"
            }
        }
    }
}