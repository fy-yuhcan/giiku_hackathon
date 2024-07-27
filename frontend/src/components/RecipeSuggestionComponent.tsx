import React, { useContext, useState } from 'react';
import RecipeSuggestion from './RecipeSuggestion';
import RecipeWindow from './RecipeWindow';
import SmallButton from './SmallButton';
import { UserContext } from '../context/userContext';
import useSWR from 'swr';
import { RecipePutType } from '../materialType';
import useSWRMutation from 'swr/mutation';
import { PageContext, pageModeType } from '../context/pageContext';

export default function RecipeSuggestionComponent() {

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
    {
      recipe_id: 4,
      text: "sample text4",
      title: "sample title4"
    },
  ]

  const fetcher = (url: string) => {
    fetch(url)
    .then(res => res.json())
  }

  const fridge: pageModeType = "fridge"
  const { user, setUser } = useContext(UserContext)
  const { pageMode, setPageMode } = useContext(PageContext)
  const { data, error, isLoading } = useSWR(`/recipe?user_id=${user.user_id}`, fetcher)
  //if (error) return <div>failed to load</div>
  //if (isLoading) return <div>loading...</div>

  const [showRecipe, setShowRecipe] = useState<number>(-1);

  const ShowRecipe = (recipe_id: number) => {
    setShowRecipe(recipe_id)
  }

  const dropRecipe = () => {
    setShowRecipe(-1)
  }

  //fetcher
  const createSuggestion = async (url: string, {arg}: {arg: RecipePutType}) => {
    await fetch(url, {
      method: 'PUT',
      body: JSON.stringify(arg)
    })
  }

  //useSWR定義
  const { trigger, isMutating } = useSWRMutation("/recipe/", createSuggestion)


  //「作った」ボタンを押したらapiを呼び出し
  const handleCooked = async(recipe_id: number) => {
    await trigger({user_id: user.user_id, recipe_id: recipe_id})
    setPageMode(fridge)
  }


  if (showRecipe > 0) {
    for (let i = 0; i < dummy_data.length; i++) {
      if (dummy_data[i].recipe_id === showRecipe) {
        return (
          <>
            <RecipeWindow content={dummy_data[i].text} />
            <SmallButton handler={dropRecipe} label={"戻る"} />
            <SmallButton handler={() => handleCooked(showRecipe)} label={"作った！"} />
          </>
        )
      }
    }
  } else {
    return (
      <>
        <RecipeSuggestion />
        <h1 className="text-xl font-bold my-4">過去に作ったレシピから選ぶ</h1>
        <div className="grid grid-cols-2 gap-4 w-3/4 mb-8">
          {
            dummy_data.map((record, index) => (
              <div
                className="bg-white p-4 text-center rounded-lg cursor-pointer hover:bg-gray-200"
                key={index}
                onClick={() => ShowRecipe(record.recipe_id)}
              >
                {record.title}
              </div>
            ))
          }
        </div>
      </>
    );
  }
}

