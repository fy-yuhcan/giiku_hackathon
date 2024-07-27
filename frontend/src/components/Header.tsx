'use client';

import React, { useContext } from 'react';
import Image from 'next/image';
import { PageContext, pageModeType } from '../context/pageContext';

export default function Header() {
  const {pageMode, setPageMode} = useContext(PageContext)
  const home: pageModeType = "home";
  const fridge: pageModeType = "fridge";

  const handleToHome = () => {
    setPageMode(home)
  }
  const handleToFridge = () => {
    setPageMode(fridge)
  }

  return (
    <header className="flex-shrink-0 bg-yellow-300 p-4">
      <div className="flex items-center justify-between">
        <div onClick={handleToHome}>
          <h1 className="text-3xl font-bold text-orange-500">食マネ</h1>
          <p className="text-lg text-orange-400">食材マネージャー</p>
        </div>
        <div className="flex space-x-8 items-center">
          <div className="flex flex-col items-center" onClick={handleToHome}>
            <Image src='/img/home.png' alt="ホーム" width={24} height={24} />
            <p className="text-sm">ホーム</p>
          </div>
          <div className="flex flex-col items-center" onClick={handleToFridge}>
            <Image src='/img/ninjin.png' alt="冷蔵庫" width={24} height={24} />
            <p className="text-sm">冷蔵庫</p>
          </div>
        </div>
      </div>
    </header>
  );
};
