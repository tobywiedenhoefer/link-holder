import React, {useEffect, useState} from "react";
import axios from "axios"

import ICard from "../interfaces/iCard";
import "../cards.css"

export const Home = () => {
    const [message, setMessage] = useState('')
    const [cards, setCards] = useState<ICard[]>([])
    useEffect(() => {
        if (localStorage.getItem('access_token') === null) {
            window.location.href = '/login'
        }
        else {
            (async () => {
                try {
                    const token = localStorage.getItem('access_token')
                    const {data} = await axios.get(
                        'http://localhost:8000/home/',
                        {
                            headers: {
                                'Content-Type': 'application/json',
                                'Authorization': `Bearer ${token}`
                            }
                        }
                    )
                    setMessage(data.message)
                    setCards([...cards, ...data.cards])
                } catch (e) {
                    console.log('not auth')
                }
            })()
        }
    }, [])
    return (
        <div className="form-signin mt-5 text-center">
            <h3 className="home-title">Hi {message}</h3>
            <div className="cards">
                {cards.map((card) => {
                    return (
                        <div className="card" key={card.card_id}>
                            <h3 className="card-title">
                                {card.link}
                            </h3>
                            <p className="card-description">
                                {card.description}
                            </p>
                            <footer className="tags">
                                {card.tags.map((tag) => {
                                    return (
                                        <a href="#" className="tag">#{tag}</a>
                                    )
                                })}
                            </footer>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}