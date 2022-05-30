import React, { useState } from "react"
import ReactDOM from "react-dom/client"
import "./index.css"

const axios = require('axios')


function Main() {

    const [link, setLink] = useState('')
    const [url, setUrl] = useState('')

    // async function requisitar() {
    //     await axios.get('http://127.0.0.1:5000/requisitar').then(function (response) { 

    //         setUrl(response.data.link)

    //     }).catch(function (error) {
    //         console.log(error)
    //     })
    // }


    async function save() {

        await axios.post('http://localhost:5000/savelink', JSON.parse(`{"link": "${link}" }`)).then((response) => {
            console.log(response.data)
            if (response.data) {
                // requisitar()
                setUrl(response.data.link)
            }
        })

        //requisitar()
        //console.log('save')
        // setTimeout(() => {  requisitar(); }, 100);

    }

    async function copyText (){
        let TextoCopiado = url
        await navigator.clipboard.writeText(TextoCopiado);
        alert('Texto copiado: '+ TextoCopiado)
        
    
    }



    return (<div className="father">
        <Head />
        <section>
            <span className="h510p">Cole a URL a ser Encurtada</span>
            <div className="form">
                <input onChange={(e) => setLink(e.target.value)} placeholder="Cole a URL aqui"></input>
                <button onClick={save} className="button">Encurtar URL</button>
            </div>
            <p>Encurtador.com é uma ferramenta gratuita para encurtar uma URL ou reduzir um link. <br />
                Use nosso encurtador de URL para criar um link encurtado, facilitando o uso.</p>


        </section>
        {url &&
            <Showurl url={url} onClick={copyText} />
        }
        <Footer />
    </div>)



}

function Head() {

    return (
        <div>
            <header>
                <a href="#" className="logo">Encurtador de URL</a>
            </header>

        </div>


    )

}

function Showurl(props) {
    return (
        <section>
            <span className="h510p">Aqui está seu link</span>
            <div className="showurl">
                <p>
                    <a href={props.url} className="teste" target="blank">{props.url}</a>
                </p>
                <button className="button" onClick={() => props.onClick()}>Copiar Link</button>
            </div>
        </section>
    )
}

function Footer(){
    return <footer>Desenvolvido por Rodrigo</footer>
}
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />)