#### vgg16
- ニューラルネットは、trainingに使った画像の特徴と、ラベルを結び付ける
- ニューラルネットは決まったInput shapeを要求する
- Kerasはミドルエンド, Tensorflowはバックエンド
- 環境構築は、辛くて厳しい (Macなら楽かも？)

#### cv2_face
- 認識と検知

#### mnist_mlp
- データは訓練用と検証用を分けるのが掟
- shapeの把握と操作
- 数字を限定してみよう ～ Forループはおすすめできない
  - 配列はスライスで切り出す
  - ndarrayのBoolean indexing　
