import React, {useEffect, useState, KeyboardEvent, ChangeEvent} from "react";
import axios from "axios"

import ICard from "../interfaces/iCard";
import "../cards.css"


async function getCardsFromAPI (searchTags: string[]) {
    const token = localStorage.getItem('access_token')
    const {data} = await axios.post(
        'http://localhost:8000/home/',
        {
            search: searchTags.length !== 0,
            tags: searchTags
        },
        {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        }
    )
    return data.cards
}

export const Home = () => {
    const [cards, setCards] = useState<ICard[]>([])
    const [search, setSearch] = useState('')
    const [searchTags, setSearchTags] = useState<string[]>([])

    const isValidSearch = () => {
        return search !== '' && !searchTags.map((searchTag) => searchTag.toUpperCase()).includes(search.toUpperCase())
    }
    const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
        if (e.key === 'Enter' && isValidSearch()) {
            setSearchTags([...searchTags, search])
            setSearch('')
        }
    }
    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        setSearch(e.target.value)
    }
    useEffect(() => {
        if (localStorage.getItem('access_token') === null) {
            window.location.href = '/login'
        }
        else {
            (async () => {
                try {
                    const reqCards = await getCardsFromAPI(searchTags)
                    setCards([...reqCards])
                } catch (e) {
                    console.log('not auth')
                }
            })()
        }
    }, [searchTags])
    return (
        <div className="form-signin mt-5 text-center">
            <div className="d-flex searchbar">
                <input
                    className="form-control me-2"
                    type="search"
                    placeholder="Search"
                    aria-label="Search"
                    onChange={handleChange}
                    onKeyDown={handleKeyDown}
                    value={search}
                    />
            </div>
            <div className="d-flex search-tags">
                {searchTags.map((searchTag) => {
                    return (
                        <p
                            className="search-tag"
                            onClick={(e) => {
                                if (searchTags.includes(searchTag)) {
                                    const tagIndex = searchTags.indexOf(searchTag)
                                    searchTags.splice(tagIndex, 1)
                                    setSearchTags([...searchTags])
                                }
                            }}
                        >{searchTag}</p>
                    )
                })}
            </div>
            <div className="cards">
                {cards
                    .map((card) => {
                    return (
                        <div className="card" key={card.card_id}>
                            <h3 className="card-title">
                                <a href={card.link || "#"}>{card.title}</a>
                            </h3>
                            <p className="card-description">
                                {card.description}
                            </p>
                            <footer className="tags">
                                {card.tags.map((tag) => {
                                    return (
                                        <span
                                            className="tag"
                                            onClick={(e) => {
                                                if (!searchTags.includes(tag)) {
                                                    setSearchTags([...searchTags, tag])
                                                }
                                            }}
                                        >#{tag}</span>
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