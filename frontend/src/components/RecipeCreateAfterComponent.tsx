import React, { useContext } from 'react';
import RecipeWindow from './RecipeWindow';
import SmallButton from './SmallButton';
import { PageContext, pageModeType } from '../context/pageContext';
import { RecipePutType } from '../materialType';
import useSWRMutation from 'swr/mutation';
import { UserContext } from '../context/userContext';
import { RecipePostResponseContext } from '../context/recipeContext';

export default function RecipeCreateAfter() {

  //const content: string = "apiをたたいて参照した文字列"
  const recipeSuggestion: pageModeType = "recipeSuggestion"
  const fridge: pageModeType = "fridge"
  const { pageMode, setPageMode } = useContext(PageContext)
  const { user, setUser } = useContext(UserContext)
  const {recipePostResponse, setRecipePostResponse} = useContext(RecipePostResponseContext)


  const handleBack = () => {
    setPageMode(recipeSuggestion)
  }

  //fetcher
  const createSuggestion = async (url: string, {arg}: {arg: RecipePutType}) => {
    await fetch(url, {
      method: 'PUT',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(arg)
    })
  }

  //useSWR定義
  const { trigger, data, error } = useSWRMutation("http://127.0.0.1:8000/recipe/", createSuggestion)


  //「作った」ボタンを押したらapiを呼び出し
  const handleCooked = async() => {
    await trigger({user_id: user.user_id, recipe_id: recipePostResponse["id"]})
    setPageMode(fridge)
  }


  return (
    <>
      <RecipeWindow content={recipePostResponse["content"]} />
      <div className="flex space-x-2">
        <SmallButton handler={handleBack} label={"戻る"} />
        <SmallButton handler={handleCooked} label={"作った！"} />
      </div>
    </>
  );
}
