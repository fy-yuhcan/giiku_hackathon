import React, { useContext } from 'react';
import RecipeWindow from './RecipeWindow';
import SmallButton from './SmallButton';
import { PageContext, pageModeType } from '../context/pageContext';

export default function RecipeCreateAfter() {

  const content: string = "apiをたたいて参照した文字列"
  const recipeSuggestion: pageModeType = "recipeSuggestion"
  const { pageMode, setPageMode } = useContext(PageContext)

  const handleBack = () => {
    setPageMode(recipeSuggestion)
  }

  const handleCooked = () => {
    // 作った！ボタンの処理をここに追加

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
