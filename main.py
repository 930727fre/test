from flask import Flask, request, jsonify
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

app = Flask(__name__)

# Initialize the tokenizer and retriever
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", use_dummy_dataset=True)
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq")

@app.route('/rag', methods=['POST'])
def rag():
    data = request.json
    question = data.get('question')

    # Encode the input question
    inputs = tokenizer(question, return_tensors='pt')
    
    # Retrieve relevant documents
    docs = retriever(inputs['input_ids'], inputs['attention_mask'])

    # Generate the answer
    output = model.generate(inputs['input_ids'], docs['input_ids'])
    answer = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
