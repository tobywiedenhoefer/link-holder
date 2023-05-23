export default interface ICard {
    user_id: string,
    card_id: string,
    link: string,
    description: string,
    tags: string[],
    collection: number
    title: string
}