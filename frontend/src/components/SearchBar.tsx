import React, {useState} from 'react';

interface SearchProps {
    onChange: (text: string) => void
}

const SearchBar = ({onChange,}: SearchProps) => {
    const [search, setSearch] = useState('')
    return (
        <div className="d-flex searchbar">
            <input
                className="form-control me-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
                onChange={(e) => {setSearch(e.target.value)}}
                value={search}
            />
        </div>
    )
}

export default SearchBar