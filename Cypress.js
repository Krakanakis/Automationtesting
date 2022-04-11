describe('Add product to cart', () => {

    it("login test", () => {
        
        cy.visit('https://www.worten.pt/')
        cy.wait(50)
        cy.contains('Aceitar Tudo').then( acceptcookies => {
            cy.wrap(acceptcookies).click()
        })

        cy.contains('.nav-login', 'INICIAR SESSÃO').then( newaccount => {
            cy.wrap(newaccount).click()
        })

        cy.get('[name="username"][type="email"]').then( username => {
            cy.wrap(username).type('XXXX@XXXX.com')
        })

        cy.get('[name="password"][type="password"]').then( username => {
            cy.wrap(username).type('XXXX')
        })

        cy.contains('[type="submit"]', 'Iniciar Sessão').click()

        cy.get('[href="/promocoes"][role="menuitem"]').click()
        cy.get('[data-index="2"]').click()
        cy.contains('Adicionar ao Carrinho').click()
        cy.wait(50)
        //cy.contains('button', 'Não, Obrigado ').click()
        cy.get('body > div.mfp-wrap.mfp-close-btn-in.mfp-auto-cursor.mfp-ready > div > div.mfp-content > div > section > div > div.w-modal__footer > div.w-modal__footer__checkout-button > a > button').click({force:true})
    })
})
