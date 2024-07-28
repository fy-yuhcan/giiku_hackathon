import dynamic from 'next/dynamic';
import React, { useContext, useRef } from 'react';
import { PageContext, pageModeType } from '../context/pageContext';
import SmallButton from './SmallButton';
import { UserContext } from '../context/userContext';
import useSWRMutation from 'swr/mutation';
import { RecipePostResponseContext } from '../context/recipeContext';

// BackButtonコンポーネントを動的にインポート（クライアントサイドでのみ使用）
const BackButton = dynamic(() => import('./BackButton'), { ssr: false });

export default function RecipeSuggestion() {

  //context初期化
  const { pageMode, setPageMode } = useContext(PageContext);
  const { user, setUser } = useContext(UserContext);
  const { recipePostResponse, setRecipePostResponse } = useContext(RecipePostResponseContext);

  //ref初期化
  const refNumServings = useRef(1)
  const refIsUseStorageOnly = useRef<string>('true')
  const refComment = useRef("")

  // 遷移先のパスを指定
  const RecipeCreateAfter: pageModeType = "RecipeCreateAfter";
  const home: pageModeType = "home"; 


  //refの値書き換えハンドラたち
  const handleChangeServings = (event: React.ChangeEvent<HTMLSelectElement>) => {
    refNumServings.current = parseInt(event.target.value)
  }
  const handleIsUseStorageOnly = (event: React.ChangeEvent<HTMLInputElement>) => {
      refIsUseStorageOnly.current = event.target.checked?'false':'true'
  }
  const handleComment = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    refComment.current = event.target.value
  }

  //fetcher
  const createSuggestion = async (url: string, {arg}: {arg: {
    user_id: number,
    num_servings: number,
    uses_storages_only: string,
    comment: string
}}): Promise<Response> => {
    const res = await fetch(url, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(arg)
    })
    return res.json()
  }

  //useSWR定義
  const { trigger, data } = useSWRMutation("http://127.0.0.1:8000/recipe/", createSuggestion)

  //作成ボタン押したときの処理
  const handleSubmit = async () => {
    const res = await trigger({
      user_id: user.user_id,
      num_servings: refNumServings.current,
      uses_storages_only: refIsUseStorageOnly.current,
      comment: refComment.current
    })
    console.log(res)

    //チャットGPTに投げた後の処理
    if (res) {
      setRecipePostResponse(res);
    } else {
      throw new Error("response not found.")
    }
    
    setPageMode(RecipeCreateAfter);
  };

  return (
    <div className="flex flex-col items-center justify-center py-10 bg-yellow-100">
      <div className="absolute top-28 left-8">
        <BackButton pageChangeTo={home} /> {/* 戻るボタンを追加 */}
      </div>
      <div className="text-center w-7/8 max-w-2xl">
        <h2 className="text-2xl font-bold mb-4">あなただけのレシピを作成します</h2>
        <textarea
          className="border rounded p-2 mb-4 w-full h-24"
          placeholder="現在の気分や体調を入力してください あっさりしたものが食べたい気分 など…"
          onChange={(event) => handleComment(event)}
        />
        <div className="mb-4">
          <select className="border rounded p-2 w-full" onChange={(event) => handleChangeServings(event)}>
            <option value="1">1人前</option>
            <option value="2">2人前</option>
            <option value="3">3人前</option>
            <option value="4">4人前</option>
            <option value="5">5人前</option>
          </select>
        </div>
        <div className="flex items-center justify-center mb-4">
          <SmallButton handler={handleSubmit} label={"作成!"} />
          <label className="ml-2">
            <input type="checkbox" className="mr-1" onChange={(event) => handleIsUseStorageOnly(event)}/>
            冷蔵庫にある食材のみを使う
          </label>
        </div>
      </div>
    </div>
  );
}
