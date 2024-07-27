"use client"; // これをファイルの先頭に追加

import React, { useState } from 'react';

export default function LoginComponent() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (event) => {
    event.preventDefault();

    // ログインのためのAPI呼び出し
    const response = await fetch('/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    if (response.ok) {
      // ログイン成功
      // 必要に応じてリダイレクトや状態の変更を行う
    } else {
      // ログイン失敗
      setError('ログインに失敗しました。ユーザー名またはパスワードが正しくありません。');
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-6 rounded-lg shadow-md w-3/4 max-w-md">
        <h2 className="text-2xl font-bold text-center mb-4">ログイン</h2>
        {error && <div className="text-red-500 mb-4">{error}</div>}
        <form onSubmit={handleLogin}>
          <div className="mb-4">
            <label className="block mb-2">ユーザー名</label>
            <input
              type="text"
              className="border rounded p-2 w-full"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="mb-4">
            <label className="block mb-2">パスワード</label>
            <input
              type="password"
              className="border rounded p-2 w-full"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <div className="text-center">
            <button type="submit" className="bg-blue-500 text-white rounded p-2 w-full">
              ログイン
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
