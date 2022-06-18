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

    function verificar_link(){
        var posicao_do_ponto = link.lastIndexOf('.')
        var str_dps_ponto = link.slice(posicao_do_ponto + 1)
        
        if(posicao_do_ponto !== -1 && link !== "" && str_dps_ponto.length >= 1){
            save()
        } else{
            alert(link + " não é um link válido.")
            setLink('')
        }
    }

    async function copyText() {
        await navigator.clipboard.writeText(url);
        alert('Texto copiado: ' + url)

    }

    return (<div className="father">
        <Head />
        <section>
            <span className="span">Cole a URL a ser Encurtada</span>
            <div className="form">
                <input onChange={(e) => setLink(e.target.value)} placeholder="Cole a URL aqui" value={link}></input>
                <button onClick={verificar_link} className="button">Encurtar URL</button>
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