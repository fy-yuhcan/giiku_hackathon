import React, { useContext } from 'react';
import RecipeWindow from './RecipeWindow';
import SmallButton from './SmallButton';
import { PageContext, pageModeType } from '../context/pageContext';
import { RecipePutType } from '../materialType';
import useSWRMutation from 'swr/mutation';
import { UserContext } from '../context/userContext';
import { SuggestionRecipeIdContext } from '../context/recipeContext';

export default function RecipeCreateAfter() {

  const content: string = "apiをたたいて参照した文字列"
  const recipeSuggestion: pageModeType = "recipeSuggestion"
  const fridge: pageModeType = "fridge"
  const { pageMode, setPageMode } = useContext(PageContext)
  const { user, setUser } = useContext(UserContext)
  const {suggestionRecipeId, setSuggestionRecipeId} = useContext(SuggestionRecipeIdContext)


  const handleBack = () => {
    setPageMode(recipeSuggestion)
  }

  //fetcher
  const createSuggestion = async (url: string, {arg}: {arg: RecipePutType}) => {
    await fetch(url, {
      method: 'PUT',
      body: JSON.stringify(arg)
    })
  }

  //useSWR定義
  const { trigger, data, error } = useSWRMutation("/recipe/", createSuggestion)


  //「作った」ボタンを押したらapiを呼び出し
  const handleCooked = async() => {
    await trigger({user_id: user.user_id, recipe_id: suggestionRecipeId})
    setPageMode(fridge)
  }

  return (
    <>
      <RecipeWindow content={content} />
      <div className="flex space-x-2">
        <SmallButton handler={handleBack} label={"戻る"} />
        <SmallButton handler={handleCooked} label={"作った！"} />
      </div>
    </>
  );
}
