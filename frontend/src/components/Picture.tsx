import React from 'react';
import useSWRMutation from 'swr/mutation';

export default function Picture() {
  //写真をバックエンドに保存するフェッチ
  async function updateImage(url:string, { arg }: {arg: {path: }}) {
    fetch(url, {
      method: "POST",
      body: JSON.stringify({
        user_id: arg.user_id,
        foods: arg.foods
      })
    })
    .then(res => res.json())
  }
  const { trigger, isMutating } = useSWRMutation("/fridge", updateImage)
  
  const handleSubmit = async (event) => {
    await trigger({user_id: user.user_id, foods: 
      ingredients.map(ingredient => {return {food_id: 0, quantity: ingredient.quantity}})
    })
    handlePageChange()
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md w-3/4 max-w-lg mx-auto mt-10">
      <div className="border-2 border-gray-300 p-4 rounded-md w-full h-64 flex items-center justify-center">
        <span className="text-gray-400">写真</span>
      </div>
    </div>
    );
}
