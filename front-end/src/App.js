import React, { useState } from "react"
import Head from "./components/Head/Head"
import Footer from "./components/Footer/Footer"
import Showurl from "./components/ShowUrl/Showurl"

const axios = require('axios')

export default function App() {

    const [url, setUrl] = useState('')
    const [link, setLink] = useState('')

    async function save() {

        const { data } = await axios.post('http://localhost:5000/savelink', ({ link: link }))
        setUrl(data.link);
        setLink('')
    }

    async function copyText() {
        let TextoCopiado = url
        await navigator.clipboard.writeText(TextoCopiado);
        alert('Texto copiado: ' + TextoCopiado)

    }

    return (<div className="father">
        <Head />
        <section>
            <span className="span">Cole a URL a ser Encurtada</span>
            <div className="form">
                <input onChange={(e) => setLink(e.target.value)} placeholder="Cole a URL aqui" value={link}></input>
                <button onClick={save} className="button">Encurtar URL</button>
            </div>
            <p>Encurtador.com é uma ferramenta gratuita para encurtar uma URL ou reduzir um link. <br />
                Use nosso encurtador de URL para criar um link encurtado, facilitando o uso.
            </p>
        </section>
        {url &&
            <Showurl url={url} onClick={copyText} />
        }
        <Footer />
    </div>)
}