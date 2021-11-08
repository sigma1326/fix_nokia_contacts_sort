import vcfpy

# Open input, add FILTER header, and open output file
reader = vcfpy.Reader.from_path('contacts/1.vcf')
# reader.header.add_filter_line(vcfpy.OrderedDict([('ID', 'DP10'), ('Description', 'total DP < 10')]))
# writer = vcfpy.Writer.from_path('/dev/stdout', reader.header)

print(reader.header)

# for record in reader:
#     print(reader)
    # ad = sum(c.data.get('DP', 0) for c in record.calls)
    # if ad < 10:
    #     record.add_filter('DP10')
    # writer.write_record(record)
