# MergeEventDetection

[Get_Mergeable_Lambda](https://github.com/SampleUser0001/Get_Mergeable_Lambda)を呼び出す。  
[Get_Mergeable_Lambda](https://github.com/SampleUser0001/Get_Mergeable_Lambda)は引数のeventで指定したリポジトリ、ブランチ間のマージが可能かどうかを取得するが、トリガーをAWS CodeCommit - > Amazon SNSなどにすると、引数として渡すeventを制御できない。  
AWS CodeCommit -> Amazon SNSから、このAWS Lambdaを呼び出すことによって、[Get_Mergeable_Lambda](https://github.com/SampleUser0001/Get_Mergeable_Lambda)に渡す起動引数を制御する。

## 参考

- [Get_Mergeable_Lambda](https://github.com/SampleUser0001/Get_Mergeable_Lambda)
- [AWS LambdaからLambdaを非同期で呼び出す(Python):Qiita](https://qiita.com/ume1126/items/8170a10fad6b21f0f54a)