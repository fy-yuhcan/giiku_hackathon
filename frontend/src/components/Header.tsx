import React from 'react';

const Header = () => {
  return (
    <header className="bg-yellow-300 p-4 text-center">
      <div className="flex items-center justify-center">
        <img src="/logo.png" alt="Logo" className="h-12 mr-4" />
        <div>
          <h1 className="text-3xl font-bold text-orange-500">食マネ</h1>
          <p className="text-lg text-orange-400">食材マネージャー</p>
        </div>
      </div>
    </header>
  );
};

export default Header;
