

def bubbleSort(data, draw_data):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw_data(data, ['green' if x == j or x == j +
                          1 else 'grey' for x in range(len(data))])

    draw_data(data, ['green' for x in range(len(data))])


def partition(data, head, tail, drawData):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        


    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    

    data[border], data[tail] = data[tail], data[border]
    
    return border

def quick_sort(data, head, tail, drawData):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData)

        #LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawData)

        #RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawData)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('grey')

        
        if i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray





