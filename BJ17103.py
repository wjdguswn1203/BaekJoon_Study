{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNoLEr2IP8TIIUd2XDuwgNW"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c2cq-2ujwDNR",
        "outputId": "25bd214f-ad4e-44ef-e742-4844e577eaa8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "6\n",
            "8\n",
            "10\n",
            "12\n",
            "100\n",
            "1\n",
            "1\n",
            "2\n",
            "1\n",
            "6\n"
          ]
        }
      ],
      "source": [
        "# 백준 17103: 골드바흐 파티션\n",
        "\n",
        "# 배열의 크기를 받아옴\n",
        "ary_num = int(input())\n",
        "ary = []\n",
        "\n",
        "# 배열의 크기만큼 입력을 받아옴\n",
        "for i in range(ary_num):\n",
        "  ary.append(int(input()))\n",
        "\n",
        "# int(math.sqrt(max(ary)+1))\n",
        "# 소수를 구하기\n",
        "prime_ary = []\n",
        "for i in range(2,max(ary)+1):\n",
        "  for j in range(2, i+1):\n",
        "    if j==i:\n",
        "      prime_ary.append(j)\n",
        "    if i%j == 0:\n",
        "      break\n",
        "\n",
        "# 소수끼리 더하다가, 리스트의 원소와 동일해지면 중지하고 count를 출력\n",
        "for num in ary:\n",
        "  count = 0\n",
        "  for i in prime_ary:\n",
        "    for j in prime_ary:\n",
        "      if(num == i+j):\n",
        "        count += 1\n",
        "  if count > 1:\n",
        "    count = round(count/2)\n",
        "  print(count)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Edz9VZZHAnKb"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}