from transformers import T5ForConditionalGeneration, AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM


def initialize_model(checkpoint):
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = T5ForConditionalGeneration.from_pretrained(checkpoint, device_map="auto")
    return model, tokenizer



def infer(input_text, model, tokenizer):
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
    outputs = model.generate(input_ids, max_new_tokens=200)
    out = tokenizer.decode(outputs[0])
    return out

def main():
    checkpoint = 'google/flan-t5-xxl'
    model, tokenizer = initialize_model(checkpoint)
    print('===============LOADING MODEL====================')
    print('Layers in Encoder: ', sum(p.numel() for p in model.encoder.parameters() if p.requires_grad))
    print('Layers in Decoder: ', sum(p.numel() for p in model.decoder.parameters() if p.requires_grad))

    prompt = '''

    You are an interviewer. Read the patient dialogue and respond accordingly. Pretend to be the patients neighbour 

    Patient: Hi, my name is Patient. What’s yours?
    Interviewer: Hi, my name’s Interviewer. 

    Patient: Hi, Interviewer. I live right across the way. Are you moving in today?
    Interviewer: Yes, I am.

    Patient: Well, I hope you really like it and I hope to see you soon. Uhm.. where did you move from?
    Interviewer: From Richardson.

    Patient: Richardson? Oh, I’ve heard that’s a really nice area. Are-- did you move over here for work?
    Interviewer: Yes.

    Patient: Well, I have to get to work and uhm.. I’ll see you after work. Have a great day. 
    Interviewer: Before you go, I’m new to the area. Can you tell me about this neighborhood?

    Patient: Well, I would tell you the neighborhood is really nice. Uhm.. if you’re looking for places to eat, I’m not really sure. But I would tell you at night, just make sure your car is locked. All right, have a good day. 
    Interviewer: 

    '''

    out = infer(prompt)

    print(out)


if "__name__" == main():
    main()