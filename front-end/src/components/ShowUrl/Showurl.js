export default function Showurl(props) {
    return (
        <section>
            <span className="titulo">Aqui está seu link</span>
            <div className="showurl">
                <p>
                    <a href={props.url} className="teste" target="blank">{props.url}</a>
                </p>
                <button className="button" onClick={() => props.onClick()}>Copiar Link</button>
            </div>
        </section>
    )
}