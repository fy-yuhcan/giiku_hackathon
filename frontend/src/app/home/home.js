import React from 'react';
import StorageContent from '../../components/StorageContent';
import ExpiryItems from '../../components/ExpiryItems';
import ShoppingReminder from '../../components/ShoppingReminder';
import MenuButton from '../../components/MenuButton';

const HomePage = () => {
  return (
    <div>
      <h1>ホーム画面</h1>
      <button>食材の追加</button>
      <button>ごはんを作る</button>
      <nav>
        <MenuButton />
      </nav>
    </div>
  );
};

export default HomePage;
