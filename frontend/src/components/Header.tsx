import React from 'react';
import Image from 'next/image';
import food from '../img/ninjin.png'; // 画像をインポート
import home from '../img/home.png'; // 画像をインポート

const Header = () => {
  return (
    <header className="bg-yellow-300 p-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-orange-500">食マネ</h1>
          <p className="text-lg text-orange-400">食材マネージャー</p>
        </div>
        <div className="flex space-x-8 items-center">
          <div className="flex flex-col items-center">
            <Image src={home} alt="ホーム" width={24} height={24} />
            <p className="text-sm">ホーム</p>
          </div>
          <div className="flex flex-col items-center">
            <Image src={food} alt="冷蔵庫" width={24} height={24} />
            <p className="text-sm">冷蔵庫</p>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
