import internal from "stream"

export type FoodDataType = {
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
    quantity: string | number;
    unit: string;
  }

export type RecipePostType = {
    user_id: number,
    num_servings: number,
    uses_storages_only: "true" | "false",
    comment: string
}

export type RecipePutType = {
    user_id: number,
    recipe_id: number
}