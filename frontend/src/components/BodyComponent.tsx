import React from 'react';
import { useContext } from 'react';
import { PageContext, pageModeType } from '../context/pageContext';
import AddFoodByImageComponent from './AddFoodByImageComponent';
import AddFoodByTextComponent from './AddFoodByTextComponent';
import AddFoodComponent from './AddFoodComponent';
import FridgeComponent from './FridgeComponent';
import HomeComponent from './HomeComponent';
import RecipeDetailOneComponent from './RecipeDetailOneComponent';
import RecipeSuggestionComponent from './RecipeSuggestionComponent';

export default function BodyComponent() {
      /*
  pageModeは
    "addFoodByImage", "addFoodByText"
    "addFood", "fridge", "home", 
    "recipeDetailOne", "RecipeSuggestion"
  のどれか
  */

  const [pageMode, setPageMode] = useContext<pageModeType>(PageContext)

    return (
        () => {
            switch (pageMode) {
                case "addFoodByImage":
                    <AddFoodByImageComponent/>
                    break;
                case "addFoodByText":
                    <AddFoodByTextComponent/>
                    break;
                case "addFood":
                    <AddFoodComponent/>
                    break;
                case "fridge":
                    <FridgeComponent/>
                    break;
                case "home":
                    <HomeComponent/>
                    break;
                case "recipeDetailOne":
                    <RecipeDetailOneComponent/>
                    break;
                case "recipeSuggestion":
                    <RecipeSuggestionComponent/>
                default:
                    throw new Error("Exception occured: a page is invalid")
            }   
        }
    )
}