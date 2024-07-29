import React, { useContext, useState } from 'react';
import RecipeSuggestion from './RecipeSuggestion';
import RecipeWindow from './RecipeWindow';
import SmallButton from './SmallButton';
import { UserContext } from '../context/userContext';
import useSWR from 'swr';
import { RecipePutType } from '../materialType';
import useSWRMutation from 'swr/mutation';
import { PageContext, pageModeType } from '../context/pageContext';
import { stringify } from 'querystring';

export default function RecipeSuggestionComponent() {

  const dummy_data = [
    {
      id: 1,
      content: "sample text1",
      title: "sample title1"
    },
    {
      id: 2,
      content: "sample text2",
      title: "sample title2"
    },
    {
      id: 3,
      content: "sample text3",
      title: "sample title3"
    },
    {
      id: 4,
      content: "sample text4",
      title: "sample title4"
    },
  ]

  const readRecipe = async (url: string): Promise<{
      title: string,
      content: string,
      id: number
  }[]> => {
    const res = await fetch(url)
    return res.json()
  }

  //遷移ページ指定
  const fridge: pageModeType = "fridge"

  //コンテキスト及びステート初期化
  const { user, setUser } = useContext(UserContext)
  const { pageMode, setPageMode } = useContext(PageContext)
  const [showRecipe, setShowRecipe] = useState<number>(-1);


  //fetcher
  const createSuggestion = async (url: string, {arg}: {arg: RecipePutType}) => {
    console.log(arg)
    const res = await fetch(url, {
      method: 'PUT',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(arg)
    })
    console.log(res)
    console.log(String(res))
    return String(res)
  }

  //useSWR定義
  const { trigger, isMutating } = useSWRMutation(`http://127.0.0.1:8000/recipe/`, createSuggestion)


  //「作った」ボタンを押したらapiを呼び出し
  const handleCooked = async(recipe_id: number) => {
    const res = await trigger({user_id: user.user_id, recipe_id: recipe_id})
    if (!res) {
      throw new Error("finished cooking request failed.")
    }
    setPageMode(fridge)
  }

  const handleShowRecipe = (recipe_id: number) => {
    setShowRecipe(recipe_id)
  }
  const handleDropRecipe = () => {
    setShowRecipe(-1)
  }

  //SWR初期化
  const { data, error, isLoading } = useSWR(`http://localhost:8000/recipe/${user.user_id}`, readRecipe)
  if (error) return <div>failed to load</div>
  if (isLoading) return <div>loading...</div>


  if (showRecipe > 0) {
    for (let i = 0; i < data.length; i++) {
      if (data[i].id === showRecipe) {
        return (
          <>
            <RecipeWindow content={data[i].content} />
            <SmallButton handler={handleDropRecipe} label={"戻る"} />
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
            data.map((record: {
              title: string,
              content: string,
              id: number
            }, index: number) => (
              <div
                className="bg-white p-4 text-center rounded-lg cursor-pointer hover:bg-gray-200"
                key={index}
                onClick={() => handleShowRecipe(record.id)}
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

