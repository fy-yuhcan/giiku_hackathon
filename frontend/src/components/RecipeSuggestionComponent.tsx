import React, { useContext } from 'react';
import RecipeSuggestion from './RecipeSuggestion';
import RecipeButton from './RecipeButton';
import RecipeWindow from './RecipeWindow';
import SmallButton from './SmallButton';
import { PageContext, pageModeType } from '@/context/pageContext';

export default function RecipeSuggestionComponent() {

    let content: string = ""
    const dummy_data = [
      {
        recipe_id: 1,
        text: "sample text1",
        title: "sample title1"
      },
      {
        recipe_id: 2,
        text: "sample text2",
        title: "sample title2"
      },
      {
        recipe_id: 3,
        text: "sample text3",
        title: "sample title3"
      },
    ]

    const isShowOneRecipe: boolean = false
    const handleShowOneRecipe = (recipe_id: number) => {
      for (let i = 0; i < dummy_data.length; i++) {
        if (recipe_id === dummy_data[i].recipe_id) {
          content = dummy_data[i].text
        }
      }
    }

    const recipeSuggestion: pageModeType = "recipeSuggestion"
    const {pageMode, setPageMode} = useContext(PageContext)
    
    const handleBack = () => {
      setPageMode(recipeSuggestion)
    }

    if (isShowOneRecipe) {
      return (
        <>
          <RecipeWindow content={content}/>
          <SmallButton handler={handleBack} label={"戻る"}/>
        </>
      )
    } else {
      return (
        <>
          <RecipeSuggestion/>
          <h1>過去に作ったレシピから選ぶ</h1>
          {
            dummy_data.map((recipe_id, text, title) => <RecipeButton label={title} onclick={() => handleShowOneRecipe(recipe_id)}/>)
          }
        </>
      );
    }
}