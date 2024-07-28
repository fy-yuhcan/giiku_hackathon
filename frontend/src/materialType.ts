import internal from "stream"

export type FoodType = {
    food_id: number,
    name: string,
    quantity: number,
    unit: "個" | "g" | "kg" | "ml" | "l" | "本" | "袋"
}

export type StoragePostType = {
    user_id: number,
    foods: {
        food_id: number,
        quantity: number
    }[]
}

export interface FoodItem {
    name: string;
    quantity: number;
    unit: "個" | "g" | "kg" | "ml" | "l" | "本" | "袋";
  }

export type RecipePostRequestType = {
    user_id: number,
    num_servings: number,
    uses_storages_only: string,
    comment: string
}

export type RecipePostResponseType = {
    title: string,
    foods: FoodType[]
    content: string,
    id: number
}

export type RecipePutType = {
    user_id: number,
    recipe_id: number
}

export type StorageGetType = {
    storage_id: number,
    food_id: number,
    name: string,
    unit: string,
    quantity: number,
    added_at: string
}