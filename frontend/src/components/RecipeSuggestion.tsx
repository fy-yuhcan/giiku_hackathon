import dynamic from 'next/dynamic';
import React, { useContext } from 'react';
import { PageContext, pageModeType } from '../context/pageContext';
import SmallButton from './SmallButton';

// BackButtonコンポーネントを動的にインポート（クライアントサイドでのみ使用）
const BackButton = dynamic(() => import('./BackButton'), { ssr: false });

export default function RecipeSuggestion() {
  const { pageMode, setPageMode } = useContext(PageContext);
  const recipeDetailOne: pageModeType = "recipeDetailOne";
  const home: pageModeType = "home"; // 遷移先のパスを指定

  const handleInputQuery = () => {
    /* APIたたく */
    setPageMode(recipeDetailOne);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-yellow-100">
      <div className="absolute top-28 left-8">
        <BackButton pageChangeTo={home} /> {/* 戻るボタンを追加 */}
      </div>
      <div className="text-center w-7/8 max-w-2xl">
        <h2 className="text-2xl font-bold mb-4">あなただけのレシピを作成します</h2>
        <textarea
          className="border rounded p-2 mb-4 w-full h-24"
          placeholder="現在の気分や体調を入力してください あっさりしたものが食べたい気分 など…"
        ></textarea>
        <div className="mb-4">
          <select className="border rounded p-2 w-full">
            <option value="1">1人前</option>
            <option value="2">2人前</option>
            <option value="3">3人前</option>
            <option value="4">4人前</option>
            <option value="5">5人前</option>
          </select>
        </div>
        <div className="flex items-center justify-center mb-4">
          <SmallButton handler={handleInputQuery} label={"作成!"} />
          <label className="ml-2">
            <input type="checkbox" className="mr-1" />
            冷蔵庫にある食材のみを使う
          </label>
        </div>
      </div>
    </div>
  );
}
