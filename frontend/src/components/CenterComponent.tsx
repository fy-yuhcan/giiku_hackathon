"use client";

import React from 'react';
import { useContext } from 'react';
import { PageContext, pageModeType } from '../context/pageContext';
import AddFoodByImageComponent from './AddFoodByImageComponent';
import FridgeComponent from './FridgeComponent';
import HomeComponent from './HomeComponent';
import RecipeCreateAfter from './RecipeCreateAfterComponent';
import RecipeSuggestionComponent from './RecipeSuggestionComponent';

export default function CenterComponent() {


    const { pageMode, setPageMode } = useContext(PageContext)

    switch (pageMode) {
        case "addFoodByImage":
            return <AddFoodByImageComponent/>
        case "fridge":
            return <FridgeComponent/>
        case "home":
            return <HomeComponent/>
        case "RecipeCreateAfter":
            return <RecipeCreateAfterComponent/>
        case "recipeSuggestion":
            return <RecipeSuggestionComponent/>
        default:
            throw new Error("Exception occured: a page is invalid")
        }
}

/*
pageModeは
"addFoodByImage", "addFoodByText"
"addFood", "fridge", "home",
"RecipeCreateAfter", "RecipeSuggestion"
のどれか
*/
