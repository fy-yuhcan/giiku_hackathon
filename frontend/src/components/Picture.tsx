import React, { useState } from 'react';
import useSWRMutation from 'swr/mutation';

export default function Picture() {
  
  //保存する画像のパス
  const DetectionFoodImagePath = "/storage/img/"

  async function uploadImage(url:string, { arg }: {arg: {file: string}}) {
    const formData = new FormData();
    formData.append('upload_file', arg.file)
    //写真をバックエンドに保存するapiにアクセス
    fetch(url, {
      method: "POST",
      body: formData, 
    })
    .then(res => res.json())
  }

  const { trigger, isMutating } = useSWRMutation("/fridge", uploadImage)

  const handleChangeFile = async (event) => {
    event.preventDefault();
    await trigger({file: event.target.files[0]})
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md w-3/4 max-w-lg mx-auto mt-10">
      <div className="border-2 border-gray-300 p-4 rounded-md w-full h-64 flex items-center justify-center">
        <span className="text-gray-400">写真をドロップ</span>
      </div>
        <input type='file' onChange={(event) => handleChangeFile(event)}></input>
    </div>
    );
}